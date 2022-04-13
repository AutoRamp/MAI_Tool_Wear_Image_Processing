
import cv2

start_point = (600, 50)
end_point = (650, 100)

if __name__ == '__main__':
    # Read the original image
    img = cv2.imread('Image255.jpg')
    con_img = cv2.imread('Image265.jpg')

    # Convert to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    con_img_gray = cv2.cvtColor(con_img, cv2.COLOR_BGR2GRAY)

    # Blur the image for better edge detection
    img_blur = cv2.GaussianBlur(img_gray, (21, 21), 0)
    con_img_blur = cv2.GaussianBlur(con_img_gray, (21, 21), 0)

    edges = cv2.Canny(img_blur, 50, 100)
    con_edges = cv2.Canny(con_img_blur, 50, 100)
    cv2.imshow('Edges', edges)
    cv2.imshow('Control Edges', con_edges)

    frameDelta = cv2.absdiff(img_blur, img_gray)
    conframeDelta = cv2.absdiff(con_img_blur, con_img_gray)
    cv2.imshow("FrameDelta", frameDelta)
    cv2.imshow("ControlFrameDelta", conframeDelta)

    contours, _ = cv2.findContours(edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    con_contours, _ = cv2.findContours(con_edges.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    contour_img = cv2.drawContours(img, contours, -1, (0,255,0), 3)
    con_contour_img = cv2.drawContours(con_img, con_contours, -1, (0,0,255), 3)

    cv2.imshow("Contours", contour_img)
    cv2.imshow("Control Contours", con_contour_img)

    cv2.imwrite("contours_worn_edge_mag.jpg", contour_img)
    cv2.imwrite("contours_worn_edge_mag_con.jpg", con_contour_img)
    cv2.imwrite("edges_worn_edge_mag.jpg", edges)
    cv2.imwrite("edges_worn_edge_mag_con.jpg", con_edges)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
    quit()
