from django.shortcuts import render
from .models import Weather

import matplotlib.pyplot as plt
import pandas as pd
from io import BytesIO
import base64


# Create your views here.
def index(request):
    x = [1, 2, 3, 4, 5]
    y = [1, 2, 3, 4, 5]
    # 그래프 그리기
    plt.plot(x, y)
    plt.title('test graph')
    plt.ylabel('y label')
    plt.xlabel('x label')
    
    # 그래프를 데이터로 넘기는 방법
    # 1. 그려진 객체를 반환 받아서 넘기는 방법 -> x
    # 2. 이미지로 저장하기 -> 간단하지만, 용량이 감당 x
    # 3. 버퍼(임시 공간) 활용하기

    # 1. 비어있는 버퍼 생성
    buffer = BytesIO()
    # 버퍼에 그래프를 저장
    plt.savefig(buffer, format='png')
    # 버퍼의 내용을 base64로 인코딩
    image_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8').replace('\n', '')
    buffer.close()

    context = {
        'chart_image': f'data:image/png;base64,{image_base64}'
    }
    

    return render(request, 'firsts/index.html', context)

def example(request):
    csv_path = 'firsts/data/test_data.csv'
    df = pd.read_csv(csv_path)

    for index, row in df.iterrows():
        if Weather.objects.filter(date=row['Date']).exists():
            continue
        weather = Weather(
            date = row['Date'],
            temp_avg_f = row['TempAvgF'],
            events=row['Events'] if pd.notna(row['Events']) else ""
        )
        weather.save()

    weathers = Weather.objects.all()
    context = {
        'weathers': weathers,
    }
    return render(request, 'firsts/example.html', context)