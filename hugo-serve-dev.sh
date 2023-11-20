# hugo-serve-dev-and-expose-to-network
IPADDR="$(ipconfig getifaddr en0)"
export IPADDR

echo "hugo starting on $IPADDR:1313"

cd hugo || exit

hugo server --buildDrafts --disableFastRender --bind $IPADDR --baseURL http://$IPADDR

echo "hugo stopped on $IPADDR:1313"
