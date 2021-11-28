import fitz, cv2, argparse
from pylibdmtx import pylibdmtx

def reader(pdf, csv):
    pdf_file = fitz.open(pdf)
    csv_file = open(csv, 'ab')
    for current_page_index in range(len(pdf_file)):
      for img_index,img in enumerate(pdf_file.get_page_images(current_page_index)):
        image = fitz.Pixmap(pdf_file, img[0])
        if image.height>50:
          image.save("1.png")
          img = cv2.imread('1.png')
          border = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value = [255, 255, 255]) 
          csv_file.write(pylibdmtx.decode(border)[0].data)
          csv_file.write(b'\n')
    csv_file.close()
    

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--pdf_file")
parser.add_argument("-o", "--csv_file")

args = parser.parse_args()
csv = args._get_kwargs()[0][1]
pdf = args._get_kwargs()[1][1]

reader(pdf, csv)




