def grid_img(gray_image):
    '''asks the user a set amount of columns and calculates the right number of lines accounting for the ratio of the image
    input : grayscale of the image
    output : number of columns, lines, size of a case and size of the image'''
    
    colonnes = int(input("number of columns : "))
    H, L = gray_image.shape[:2] # image dimension
    ratio = L/H
    lignes = int(colonnes/ratio/2)
    cellules_colonnes = L / colonnes 
    cellules_lignes = H / lignes 

    return (colonnes, lignes, cellules_colonnes, cellules_lignes, H, L)

def obt_clarte(gray_image):
    '''creates a grid with a set number of column and calculates the gray level of each case of the image.
    input : grayscale of an image
    return : list storing the gray level of each case'''
    colonnes, lignes, cell_col, cell_lign, H, L = grid_img(gray_image)
    clarte_grille = numpy.zeros((lignes, colonnes), dtype=float)
    
    for i in range(lignes):
        for j in range(colonnes):
            # image cropping into identical squares 
            y1 = int(i * cell_lign)
            y2 = int((i + 1) * cell_lign) if i < lignes - 1 else H
            x1 = int(j * cell_col)
            x2 = int((j + 1) * cell_col) if j < colonnes - 1 else L
            
            cell = gray_image[y1:y2, x1:x2]
            # gray level of each case
            clarte_grille[i, j] = float(cv2.mean(cell)[0])
    
    return clarte_grille

def ASCII(grille):
    '''transforms the list of gray level in ascii characters and prints the result
    input : list of gray level
    return : list of the ascii art'''

    ### exemples of lists for the render ###
    #Asciiscale = ["@", "%", "#", "*", "+", "=", "-", ":", ".", " "]
    #Asciiscale = ["$","@","B","%","8","&","W","M","#","*","o","a","h","k","b","d","p","q","w","m","Z","O","0","Q","L","C","J","U","Y","X","z","c","v","u","n","x","r","j","f","t","/",'\ ','|',"(",")","1","{","}","[","]","?","-","_","+","~","i","!","l","I",";",":",",","\ ","^","`",'"'," "]
    #Asciiscale = ["@", "#", "S", "%", "?", "*", "+", ";", ":", "."," "]
    #Asciiscale = ["$", "@", "B", "%", "8", "&", "W", "M", "#", "*", "o", "a", "h", "k", "b", "d", "p", "q", "w", "m", "Z", "O", "0", "Q", "L", "C", "J", "U", "Y", "X", "z", "c", "v", "u", "n", "x", "r", "j", "f", "t", "/", "\\", "|", "(", ")", "1", "{", "}", "[", "]", "?", "-", "_", "+", "~", "<", ">", "i", "!", "l", "I", ";", ":", ",", "\"", "^", "`", "'", "."]
    Asciiscale = ["@","o","~", ".", " "," "]
    #Asciiscale = ["∷","∷","∷","∷",":",":", ".", ".", " "," ", " "]

    aaaaa = []
    
    # conversion taux de gris en ascii
    for i in range(len(grille)):
        ligne = ""
        for j in range(len(grille[0])):
            val = int(grille[i][j]/255 * (len(Asciiscale) - 1))
            ligne += Asciiscale[val]
        aaaaa.append(ligne)

    # display of ASCII art
    for k in range(len(aaaaa)):
        print(aaaaa[k])
    
    return aaaaa

def save_ASCII (ASCII) :
    '''saves the ascii art as a .txt file in the user's dowload file
    input : string (the ascii art to save)'''
    dl_path = os.path.join(os.path.expanduser("~"), "Downloads")
    output_file = os.path.join(dl_path, "ascii_image.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        for line in ASCII:
            f.write(line + "\n")

###########################################################
import cv2
import numpy
import os



###### Load file here ######
image = cv2.imread("c:/Users/.../image.jpg")
############################

if image is None:
    raise ValueError("Unable to load file. Check the path.")
else:
    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert file to a grayscale
    clarte_grille = obt_clarte(gray_scale)
    Ascii_result = ASCII(clarte_grille)
    save_ASCII(Ascii_result)
