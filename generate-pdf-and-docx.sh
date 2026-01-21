#!/usr/bin/env zsh

# requires: python venv, pandoc, docker, docker compose

set -e

# --- Configuration ---
# The URL of the development server Hugo is running on.
# 'host.docker.internal' allows the Docker container to connect to the host machine.
DEV_SERVER_URL="http://host.docker.internal:1313"

# The public URL of your production website.
PROD_SERVER_URL="https://www.dmalo.de"

check_url() {
  local url="$1"
  local max_retries="$2"
  local retries=0
  
  until [ "$retries" -ge "$max_retries" ]; do
    if curl -s --head --fail "$url" > /dev/null; then
      return 0
    fi
    
    retries=$((retries + 1))
    sleep 5
  done
  
  echo "Error: Container at $url is not reachable after $max_retries retries"
  return 1
}

venv_folder="venv"

if [[ -d "$venv_folder" ]]; then
  echo "Using '$venv_folder' as python venv."
else
  echo "Creating a virtual environment in '$venv_folder'..."
  python3 -m venv "$venv_folder"
  echo "Virtual environment created successfully."
fi

echo "Converting markdown to docx and pdf"
echo "PDF is converted from www.dmalo.de, changes need to be live before conversion"

docker compose -f website2pdf/docker-compose.yml up -d

echo "Starting selenium docker container, waiting for availability"
check_url "http://localhost:4444" 24
echo "selenium docker container available"

source venv/bin/activate

pip install selenium
pip install pyyaml

pushd markdown2docx || exit
python export_de_portfolio_to_docx.py &
popd || exit

pushd website2pdf || exit
python py_print_to_pdf.py --dev-url "$DEV_SERVER_URL" --prod-url "$PROD_SERVER_URL" &
popd || exit

wait

docker compose -f website2pdf/docker-compose.yml down

echo "Conversion complete"
