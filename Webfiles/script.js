function myAccFunc(item) {
    let x = document.getElementById(item);
    if (x.className.indexOf("w3-show") == -1) {
      x.className += " w3-show";
      x.previousElementSibling.className += " w3-green";
    } else { 
      x.className = x.className.replace(" w3-show", "");
      x.previousElementSibling.className = 
      x.previousElementSibling.className.replace(" w3-green", "");
    }
}

var vm = new Vue({
    el: "#app",
    data: {
        values: [
            ["REPORT", 759375, 7588],
            ["PEOPLE", 759375, 1455],
            ["RUSSIA", 759375, 7277],
            ["UKRAINE", 759375, 5531],
            ["UK", 759375, 4394],
            ["PRIME", 759375, 8269],
            ["MINISTER", 759375, 5041],
            ["RISHI", 759375, 8131],
            ["SUNAK", 759375, 1088],
            ["WRITES", 759375, 290],
            ["PAUL", 100000, 9764],
            ["HITS", 100000, 9324],
            ["HAYES", 100000, 18],
            ["REPUBLICAN", 100000, 2807],
            ["LIVE", 100000, 4808],
            ["SHAY", 100000, 876],
            ["SINGER", 100000, 9386],
            ["VOTERS", 100000, 3922],
            ["LOOK", 100000, 8712],
            ["CLOSER", 100000, 9465],
            ["OFFICIALS", 100000, 4841],
            ["DEAL", 100000, 7823],
            ["MASSIVE", 100000, 1785],
            ["ATTACK", 100000, 3322],
            ["MEDIA", 100000, 9198],
            ["DEAD", 100000, 2655],
            ["MASS", 100000, 2395],
            ["EGYPT", 100000, 8692],
            ["MOMENT", 100000, 8300],
            ["SALEM", 100000, 2922]],
        colors: function(data) {
            if (data[2] <= 3000) {
              return '#497eff';
            } else if (data[2] <= 7000) {
              return '#ffdd26';
            } else {
              return '#ff4f55';
            }
        },
        styles: {
            titleFontSize: 20,
            titleFontWeight: 'bold'
        }
    },
    methods: {
        onClickEvent: function(obj, e) {
            myAccFunc(obj.data[0]);
        },
    }
});