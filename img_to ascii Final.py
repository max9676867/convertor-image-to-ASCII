import cv2
import numpy
import os


def get_grid_parameters(gray_image : numpy.ndarray):
    """prompts the user for the number of columns and calculates the number of rows,
    maintaining the image's aspect ratio. Also computes the size of each grid cell.
    
    Args : 
        gray_image (ndarray): grayscale image 
    
    Returns :
        tuple [int, int, float, float, int, int]:
            - number of columns
            - number of rows
            - width of each cell
            - height of each cell
            - total width of the image
            - total height of the image
    """
    
    columns = int(input("number of columns : "))
    Height, Width = gray_image.shape[:2] 
    ratio = Width / Height
    rows = int(columns / ratio / 2)
    cell_width = Width / columns
    cell_height = Height / rows

    return columns, rows, cell_width, cell_height, Width, Height

def compute_grid_brightness(gray_image):
    """divides the image into a grid and computes the average brightness for each cell.
    
    Args : 
        gray_image (ndarray): grayscale image
    
    Returns :
        np.ndarray : 2D array of average brightness values for each grid cell."""
    '''creates a grid with a set number of column and calculates the gray level of each case of the image.
    input : grayscale of an image
    return : list storing the gray level of each case'''
    columns, rows, cell_width, cell_height, Width, Height = get_grid_parameters(gray_image)
    brightness_grid = numpy.zeros((rows, columns), dtype=float)
    
    for i in range(rows):
        for j in range(columns):
            # image cropping into identical squares 
            y1 = int(i * cell_height)
            y2 = int((i + 1) * cell_height) if i < rows - 1 else Height
            x1 = int(j * cell_width)
            x2 = int((j + 1) * cell_width) if j < columns - 1 else Width
            
            cell = gray_image[y1:y2, x1:x2]
            # gray level of each case
            brightness_grid[i, j] = float(cv2.mean(cell)[0])
    
    return brightness_grid

def convert_to_ASCII(brightness_grid):
    """converts the brightness grid into ASCII art using predefined characters scale.
    
    Args :
        brightness_grid (np.ndarray): 2d array of brightness values
        
    Returns :
        List [str]: list of strings, each representing a line of the ASCII art.
    """

    ###### exemples of lists for the render ######
    # # darker to lighter # #
    #Asciiscale = ["@", "%", "#", "*", "+", "=", "-", ":", ".", " "]
    #Asciiscale = ["$","@","B","%","8","&","W","M","#","*","o","a","h","k","b","d","p","q","w","m","Z","O","0","Q","L","C","J","U","Y","X","z","c","v","u","n","x","r","j","f","t","/",'\ ','|',"(",")","1","{","}","[","]","?","-","_","+","~","i","!","l","I",";",":",",","\ ","^","`",'"'," "]
    #Asciiscale = ["@", "#", "S", "%", "?", "*", "+", ";", ":", "."," "]
    #Asciiscale = ["$", "@", "B", "%", "8", "&", "W", "M", "#", "*", "o", "a", "h", "k", "b", "d", "p", "q", "w", "m", "Z", "O", "0", "Q", "L", "C", "J", "U", "Y", "X", "z", "c", "v", "u", "n", "x", "r", "j", "f", "t", "/", "\\", "|", "(", ")", "1", "{", "}", "[", "]", "?", "-", "_", "+", "~", "<", ">", "i", "!", "l", "I", ";", ":", ",", "\"", "^", "`", "'", "."]
    Asciiscale = ["@","o","~", ".", " "," "]
    #Asciiscale = ["∷","∷","∷","∷",":",":", ".", ".", " "," ", " "]

    aaaaa = []
    
    for i in range(len(brightness_grid)):
        line = ""
        for j in range(len(brightness_grid[0])):
            val = int(brightness_grid[i][j]/255 * (len(Asciiscale) - 1))
            line += Asciiscale[val]
        aaaaa.append(line)

    for line in aaaaa:
        print(line)
    
    return aaaaa

def save_ASCII (ASCII_art) :
    """Saves the ASCII art as a text file in the user's Downloads directory.
    
    Args :
        ASCII_art (List[str]): list of strings representing the ASCII art
    """
    dl_path = os.path.join(os.path.expanduser("~"), "Downloads")
    output_file = os.path.join(dl_path, "ascii_image.txt")

    with open(output_file, "w", encoding="utf-8") as f:
        for line in ASCII_art:
            f.write(line + "\n")


def main():
    """
    Mains function to load the image, converts it to ASCII art and saves the result."""
    ###### Load file here ######
    image = cv2.imread("c:/Users/Maxime/Desktop/projets/vache.jpg")

    if image is None:
        raise ValueError("Unable to load file. Check the file path.")
    else:
        gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        brightness_grid = compute_grid_brightness(gray_scale)
        Ascii_result = convert_to_ASCII(brightness_grid)
        save_ASCII(Ascii_result)



if __name__ == "__main__":
    main()
