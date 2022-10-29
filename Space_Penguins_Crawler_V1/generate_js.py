import random

def generate_js(topics, tweets_frame):
    js_file = """function myAccFunc(item) {
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
            """
    first_one = True
    for t, number in topics.items():
        if not first_one:
            js_file += """,
            """
        js_file += f'["{t}", {(number * 5) ** 5}, {random.randint(1, 10001)}]'
        first_one = False

    js_file += """],
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
});"""

    return js_file
