const currentDate = new Date();

const day = String(currentDate.getDate()).padStart(2, '0');
const month = String(currentDate.getMonth() + 1).padStart(2, '0');
const year = currentDate.getFullYear();

const formattedDate = `${day}.${month}.${year}`;

const currentDateElement = document.getElementById("current-date");
currentDateElement ? currentDateElement.textContent = formattedDate : null;
