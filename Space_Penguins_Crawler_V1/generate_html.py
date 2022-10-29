import bias_allocator

def generate_html(topics, tweets_frame):
    html_file = r"""<!doctype html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="https://www.w3schools.com/w3css/4/w3.css">
    <link rel="stylesheet" href="style.css">
    <title>Document</title>
</head>
<body>
    <header>
        <div class="w3-sidebar w3-bar-block w3-light-grey w3-card" style="width:500px;">
            """

    for t, number in topics.items():
        html_file += f"""<div id="{t}" class="w3-hide w3-white w3-card">
                <p class="w3-center" style="padding-top:5px;">{t}</p>
                """

        for index, article in tweets_frame.iterrows():
            if t.upper() not in article['Tweet'].upper():
                continue

            result = bias_allocator.assess_handle(article['Source'])
            html_file+= f"""<div class="w3-margin-top w3-margin-bottom" style="border-style: outset">
                    <div class="w3-bar-item w3-margin-left">{article['Tweet']}</div>
                    <a href="{article['Link']}" class="w3-bar-item w3-button w3-text-blue">Link</a>
                    <div class="w3-bar-item w3-margin-left w3-margin-bottom">Reliability: {"N/A" if len(result["reliability"]) == 0 else result["reliability"][0]["rating"]}   <button onclick="myFunction()">Click to expand</button></div>
                        <div class="w3-margin-left w3-margin-bottom myDIV"> 
                            <p>Rating: {"N/A" if len(result["reliability"]) == 0 else result["reliability"][0]["rating"]} | <a href="#">{"N/A" if len(result["reliability"]) == 0 else result["reliability"][0]["source"]}</a></p>
                        </div>

                        <div class="w3-bar-item w3-margin-left w3-margin-bottom">Political bias: {"N/A" if len(result["leaning"]) == 0 else result["leaning"][0]["rating"]}   <button onclick="myFunction2()">Click to expand</button></div>
                        <div class="w3-margin-left w3-margin-bottom myDIV2">
                            <p>Rating: "{"N/A" if len(result["leaning"]) == 0 else result["leaning"][0]["rating"]}" | <a href="#">{"N/A" if len(result["leaning"]) == 0 else result["leaning"][0]["source"]}</a></p>
                        </div>
                    </div>
            """


        html_file += """</div>
        """

    html_file += """
        </div>
    </header>
    <div id="app" class="w3-right">
        <graph-bubblecloud
                  :width="1000"
                  :height="800"
                  :padding-top="5"
                  :padding-bottom="0"
                  :padding-left="0"
                  :padding-right="0"
                  :values="values"
                  :colors="colors"
                  :styles="styles"
                  :render-interval="0"
                  @click="onClickEvent">
          </graph-bubblecloud>
    </div>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/vue/2.5.16/vue.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/vue-graph@0.5.3/dist/vue-graph.js"></script>
    <script src="script.js"></script>
    <script>
        function myFunction() {
            var x = document.getElementsByClassName("myDIV");
            Array.from(x).forEach((el) => {
                if (el.style.display === "block") {
                    el.style.display = "none";
            } else {
                el.style.display = "block";
            }})

        }

        function myFunction2() {
            var x = document.getElementsByClassName("myDIV2");
            Array.from(x).forEach((el) => {
                if (el.style.display === "block") {
                    el.style.display = "none";
            } else {
                el.style.display = "block";
            }})
        }
    </script>
    <link rel="stylesheet" href="style.css">
</body>
</html>"""

    return html_file
