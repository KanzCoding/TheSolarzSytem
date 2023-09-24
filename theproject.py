import cv2


img = cv2.imread("solar-system.jpg")


planet_text = [
    {"name": "Sun", "font": cv2.FONT_HERSHEY_SIMPLEX, "font_scale": 1, "color": (0, 255, 255), "position": (0, 50)},
    {"name": "Mercury", "font": cv2.FONT_HERSHEY_SIMPLEX, "font_scale": 0.5, "color": (255, 0, 0), "position": (110, 185)},
    {"name": "Venus", "font": cv2.FONT_HERSHEY_SIMPLEX, "font_scale": 0.5, "color": (188, 103, 13), "position": (185, 180)},
    {"name": "Earth", "font": cv2.FONT_HERSHEY_SIMPLEX, "font_scale": 0.5, "color": (0, 255, 0), "position": (285, 170)},
    {"name": "Mars", "font": cv2.FONT_HERSHEY_SIMPLEX, "font_scale": 0.5, "color": (255, 154, 0), "position": (380, 170)},
    {"name": "Jupiter", "font": cv2.FONT_HERSHEY_SIMPLEX, "font_scale": 0.5, "color": (255, 255, 0), "position": (570, 65)},
    {"name": "Saturn", "font": cv2.FONT_HERSHEY_SIMPLEX, "font_scale": 0.5, "color": (255, 255, 0), "position": (775, 110)},
    {"name": "Uranus", "font": cv2.FONT_HERSHEY_SIMPLEX, "font_scale": 0.5, "color": (0, 255, 0), "position": (960, 130)},
    {"name": "Neptune", "font": cv2.FONT_HERSHEY_SIMPLEX, "font_scale": 0.5, "color": (255, 255, 255), "position": (1110, 130)},
]


for planet in planet_text:
    cv2.putText(img, planet["name"], planet["position"], planet["font"], planet["font_scale"], planet["color"], 2, cv2.LINE_AA)

cv2.imshow("output", img)


cv2.waitKey(0)





