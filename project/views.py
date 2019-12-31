from django .shortcuts import render

def home(request):
    template_name="index.html"
    content={"name":"anuj"}
    return render(request, template_name, content)