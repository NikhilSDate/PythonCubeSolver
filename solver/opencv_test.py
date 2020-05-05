import cv2
import numpy as np
import math


def get_angle_error(shape):
    angles = list()
    for i in range(4):
        point_1 = contour[i % 4][0]
        point_2 = contour[(i + 1) % 4][0]
        point_3 = contour[(i + 2) % 4][0]
        a = np.subtract(point_1, point_2)
        b = np.subtract(point_3, point_2)
        angles.append(math.acos(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))))

    ideal_angles = [math.pi / 2, math.pi / 2, math.pi / 2, math.pi / 2]
    mean_square_error = np.square(np.subtract(angles, ideal_angles)).mean()
    return mean_square_error


def get_average_distance(test_contour, contour_list):
    test_contour_moments=cv2.moments(test_contour)
    x=int(test_contour_moments["m10"]/test_contour_moments["m00"])
    y=int(test_contour_moments["m01"]/test_contour_moments["m00"])
    test_contour_centroid=np.array([x,y])
    distances=[]
    for contour2 in contour_list:
        contour_moments=cv2.moments(contour2)
        contour2_x = int(contour_moments["m10"] / contour_moments["m00"])
        contour2_y = int(contour_moments["m01"] / contour_moments["m00"])
        contour2_centroid = np.array([contour2_x, contour2_y])
        distance=np.linalg.norm(np.subtract(contour2_centroid,test_contour_centroid))
        distances.append(distance)
    return np.mean(distances)

def get_mean_squared_distance_error(shape):
    mean=0
    for i in range(len(shape)):
        mean+=np.linalg.norm(np.subtract(shape[i],shape[(i+1)%4]))
def get_aspect_ratio(shape):
    length_1 = np.linalg.norm(np.subtract(shape[1],shape[0]))
    length_2 = np.linalg.norm(np.subtract(shape[2], shape[1]))
    return float(max(length_1,length_2)/min(length_2,length_1))
cap = cv2.VideoCapture(1)

mask = np.zeros((640, 480), dtype=np.uint8)

previous_mask = np.zeros((640, 480), dtype=np.uint8)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    blurred_image = cv2.GaussianBlur(gray, (5, 5), 0)

    edges = cv2.Canny(blurred_image, 20, 40)
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(edges, kernel, iterations=2)
    contours, hierarchy = cv2.findContours(dilated.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    filtered_contours = []
    for i in range(len(contours)):
        contour = contours[i]
        current_hierarchy = None
        if (hierarchy is None) or (hierarchy is not None and hierarchy[0][i][2] < 0):
            if cv2.contourArea(contour) > 500 and cv2.contourArea(contour) < 5000:
                epsilon = 0.1 * cv2.arcLength(contour, True)
                contour = cv2.approxPolyDP(contour, epsilon, True)
                min_distance = 640
                distance = 0
                if len(contour) == 4:
                    # for i in range(3):
                    #     distance = math.sqrt((pow(contour[i + 1][0][0] - contour[i][0][0], 2) + pow(
                    #         contour[i + 1][0][1] - contour[i][0][1], 2)))
                    #     if distance < min_distance:
                    #         min_distance = distance
                    # for i in range(2):
                    #     distance = math.sqrt((pow(contour[i + 2][0][0] - contour[i][0][0], 2) + pow(
                    #         contour[i + 2][0][1] - contour[i][0][1], 2)))
                    #     if distance < min_distance:
                    #         min_distance = distance
                    # TODO:ADD DISTANCE THRESHOLD
                    if get_angle_error(contour) < 0.5:
                        filtered_contours.append(contour.copy())
    bounding_rectangle_points=[]
    for contour in filtered_contours:
            if get_average_distance(contour,filtered_contours)<150:#TODO:IMPLEMENT OUTLIER DETECTION
                for i in range(4):
                    bounding_rectangle_points.append(contour[i][0])

                hull = cv2.convexHull(contour)

                cv2.drawContours(frame, [hull], -1, (0, 255, 0), 3)
    if len(bounding_rectangle_points)>0:
        bounding_rectangle_points=np.array(bounding_rectangle_points)
        rect = cv2.minAreaRect(bounding_rectangle_points)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        if (get_aspect_ratio(np.array(box))<1.1):
            cv2.drawContours(frame, [box], 0, (0, 0, 255), 2)

    cv2.imshow('gray', blurred_image)
    cv2.imshow('edges', dilated)
    cv2.imshow('frame', frame)
    if (cv2.waitKey(1)) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
