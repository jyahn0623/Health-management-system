from django.shortcuts import render

# 메인
def main(request):
    return render(request, 'main/index.html')

