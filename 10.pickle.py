# pickle은 라이브러리, 객체의 형태를 그대로 유지하면서 파일에 저장하고 불러올 수 있게 하는 모듈
import pickle
favorite_color = {"lion" : "yellow", "kitty": "red"}
pickle.dump(favorite_color, open("save.pkl","wb")) # dump함수를 사용
favorite_color_load = pickle.load(open("save.pkl","rb"))
print(favorite_color_load)
print(favorite_color_load["kitty"])
print(favorite_color_load["lion"])
