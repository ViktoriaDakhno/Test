import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera is not found")
    exit()
filter_mode = 0
while True:
    # flag, cadr = camera.read()
    #
    # if not flag:
    #     print("Error")
    #     break
    #
    # craya = cv2.Canny(cadr, 150, 50)
    # cv2.imshow("Craya", craya)
    #
    # cv2.imshow("WebCam", cadr)
    #
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
    ret, frame = camera.read()
    if not ret:
        print("Ошибка: Не удалось получить кадр")
        break

    if filter_mode == 1:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Ч/б
    elif filter_mode == 2:
        frame = cv2.GaussianBlur(frame, (15, 15), 0)  # Размытие
    elif filter_mode == 3:
        frame = cv2.Canny(frame, 50, 150)  # Контуры
    elif filter_mode == 5:
        frame = cv2.bitwise_not(frame)  # Инверсия

    cv2.imshow("Webcam", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):  # Выход
        break
    elif key == ord('f'):  # Переключение фильтров
        filter_mode = (filter_mode + 1) % 6
        print(f"Фильтр: {filter_mode}")

camera.release()
cv2.destroyAllWindows()