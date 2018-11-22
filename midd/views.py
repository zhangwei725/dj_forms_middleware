from django.shortcuts import render


def test1(request):
    print("view-test3")
    # t = TemplateResponse(request, 'index.html')
    # t.render()
    return render(request, 'index.html')
