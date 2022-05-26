import cv2
import holo_detector
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', required=True, choices='blog_money.mp4 jangsion_id_card.mp4'.split(), help='Name of input mp4 file name')
    return parser.parse_args()


def main():
    args = get_args()

    file_name = args.input_file
    data_dir = '../data'
    infile = f'{data_dir}/input/{file_name}'
    mix_outfile = f'{data_dir}/mix_output/{file_name}'
    heatmap_outfile = f'{data_dir}/heatmap_output/{file_name}'

    if file_name == 'jangsion_id_card.mp4':
        width, height = 1920, 1080
    else:
        width, height = 1080, 640
    cap = cv2.VideoCapture(infile)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)
    cap.set(cv2.CAP_PROP_FOCUS, 0)

    fps = cap.get(cv2.CAP_PROP_FPS)

    detector = holo_detector.HoloDetector(debug=True)
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    mix_out = cv2.VideoWriter(mix_outfile, fourcc, round(fps), (width, height))
    heatmap_out = cv2.VideoWriter(heatmap_outfile, fourcc, round(fps), (width, height))

    while cap.isOpened():
        (ret, frame) = cap.read()
        if frame is None:
            break
        holo_mask, img_holo, img_hit = detector.detect_holos(frame)
        mix_out.write(img_holo)
        heatmap_out.write(img_hit)

    mix_out.release()
    heatmap_out.release()
    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
