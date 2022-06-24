from flask import Flask, request,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/createwidget",methods=["POST"])
def createwidget():
    widget = request.form['widget']
    value = request.form['value']
    name = request.form['name']
    idw = request.form['id']
    link = request.form['link']
    try:
        disabled = request.form['disabled']
    except:
        disabled = ""
    
    if disabled == "on":
        disabled = "disabled"

    code_widget = None

    if widget == "label":
        if link == "":
            code_widget = f""" &lt;label name="{name}"&gt;{value}&lt;/label&gt; """
        else:
            code_widget = f""" &lt;a name="{name}" href="{link}"&gt;{value}&lt;/a&gt; """
    elif widget == "button":
        code_widget = f""" &lt;button name="{name}" id="{idw}" onclick="location.href='{link}'" {disabled}&gt;{value}&lt;/button&gt; """
    elif widget == "textbox":
        code_widget = f""" &lt;input type="text" name="{name}" id="{idw}" value="{value}" {disabled}&gt; """
    elif widget == "submitbutton":
        code_widget = f""" &lt;input type="submit" name="{name}" id="{idw}" value="{value}" {disabled}&gt; """
    elif widget == "resetbutton":
        code_widget = f""" &lt;input type="reset" name="{name}" id="{idw}" value="{value}" {disabled}&gt; """
    elif widget == "email":
        code_widget = f""" &lt;input type="email" name="{name}" id="{idw}" value="{value}" {disabled}&gt; """
    elif widget == "file":
        code_widget = f""" &lt;input type="file" name="{name}" id="{idw}" {disabled}&gt; """
    

    code_for_return = f'''
{code_widget}
<hr>
{code_widget.replace("&lt;","<").replace("&gt;",">")}
'''
    return code_for_return

if __name__ == "__main__":
    app.run("0.0.0.0",8000,False)