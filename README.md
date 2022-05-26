# Rule-Based(HSV) 기반 Hologram Detector

### Enviroment ( python3.7, ubuntu or windows)
```console
id@domain:~$ pip install -r requirements.txt
```
### Command
```python
python detect_holo.py --input_file {blog_money.mp4, jangsion_id_card.mp4}
```

## Folder & File description

| Filename         |           Description            |  Type   |
|------------------|:--------------------------------:|:-------:|
| detect_holo.py   |    동영상-이미지 변환 및 홀로그램 추출 실행 코드    |  Code   |
| holo_detector.py |         홀로그램 추출 알고리즘 코드          |  Code   |
| input            |           입력되는 동영상 파일            |  Data   |
| heatmap_output   | 예측된 홀로그램이 Heatmap 형태로 생성된 동영상 파일 |  Data   |
| mix_output       | 입력된 동영상에 예측된 홀로그램이 오버레이된 동영상 파일  |  Data   |
