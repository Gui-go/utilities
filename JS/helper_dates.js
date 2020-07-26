function formatDate(dayOfWeek, day, month, year) {
    var daysOfWeek = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];
    var months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
    return daysOfWeek[dayOfWeek] + " " + months[month] + " " + day + " " + year;
}
//Foo lives in a country with timezone GMT + 1
var birthday = new Date(2000, 0, 1); // Year, Month, Day
console.log("Foo was born on: " +
    formatDate(
        birthday.getDay(), birthday.getDate(), birthday.getMonth(), birthday.getFullYear()
    )
);

// ___________________________________________


function formatDate2(dayOfWeek, day, month, year) {
    var daysOfWeek = ["Domingo", "Segunda", "Terça", "Quarta", "Quinta", "Sexta", "Sábado"];
    var months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"];
    return daysOfWeek[dayOfWeek] + ", dia " + day + " de " + months[month] + " de " + year;
}

var birthday = new Date(1993, 3, 25); // Year, Month, Day
console.log("Guigo nesceu " +
    formatDate2(
        birthday.getDay(), birthday.getDate(), birthday.getMonth(), birthday.getFullYear()
    )
);

// _____________________________________________

var today = new Date().toLocaleDateString('en-GB', {
    day: 'numeric',
    month: 'short',
    year: 'numeric'
});

console.log(today)