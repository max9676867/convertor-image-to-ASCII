def grid_img(gray_image):
    '''calcule une grille de N colonnes réparties sur la longueur L et le nombre de lignes correspondant au ratio de l'image
    input : image en grayScale
    return : le nombre de colonnes, de lignes, la taille d'une cellule ainsi que la taille de l'image'''
    
    colonnes = int(input("nombre de colonnes : "))
    H, L = gray_image.shape[:2] # dimension image
    ratio = L/H
    lignes = int(colonnes/ratio/2)
    cellules_colonnes = L / colonnes 
    cellules_lignes = H / lignes 

    return (colonnes, lignes, cellules_colonnes, cellules_lignes, H, L)

def obt_clarte(gray_image):
    '''découpe l'image en une grille de N colonnes et M lignes et calcule le niveau de blanc de chaque case
    input : image en grayscale
    return : grille de niveau de blanc des cases'''
    colonnes, lignes, cell_col, cell_lign, H, L = grid_img(gray_image)
    clarte_grille = numpy.zeros((lignes, colonnes), dtype=float)
    
    for i in range(lignes):
        for j in range(colonnes):
            # découpage image en carrés identiques
            y1 = int(i * cell_lign)
            y2 = int((i + 1) * cell_lign) if i < lignes - 1 else H
            x1 = int(j * cell_col)
            x2 = int((j + 1) * cell_col) if j < colonnes - 1 else L
            
            cell = gray_image[y1:y2, x1:x2]
            # récupération clarté case
            clarte_grille[i, j] = float(cv2.mean(cell)[0])
    
    return clarte_grille

def ASCII(grille):
    """transforme la grille de niveau en blanc en caracteres ascii pour l'affichage
    input : grille de niveau de blanc
    return : none
    affichage du résultat et enregistrement sur pc utilisateur"""
    #gscale = ["@", "%", "#", "*", "+", "=", "-", ":", ".", " "]
    #gscale = ["$","@","B","%","8","&","W","M","#","*","o","a","h","k","b","d","p","q","w","m","Z","O","0","Q","L","C","J","U","Y","X","z","c","v","u","n","x","r","j","f","t","/",'\ ','|',"(",")","1","{","}","[","]","?","-","_","+","~","i","!","l","I",";",":",",","\ ","^","`",'"'," "]
    #gscale = ["@", "#", "S", "%", "?", "*", "+", ";", ":", "."," "]
    #gscale = ["$", "@", "B", "%", "8", "&", "W", "M", "#", "*", "o", "a", "h", "k", "b", "d", "p", "q", "w", "m", "Z", "O", "0", "Q", "L", "C", "J", "U", "Y", "X", "z", "c", "v", "u", "n", "x", "r", "j", "f", "t", "/", "\\", "|", "(", ")", "1", "{", "}", "[", "]", "?", "-", "_", "+", "~", "<", ">", "i", "!", "l", "I", ";", ":", ",", "\"", "^", "`", "'", "."]
    #gscale = ["@","o","~", ".", " "]
    gscale = ["∷","∷","∷","∷",":",":", ".", ".", " "," ", " "]

    aaaaa = []
    
    #conversion taux de gris en ascii
    for i in range(len(grille)):
        ligne = ""
        for j in range(len(grille[0])):
            val = int(grille[i][j]/255 * (len(gscale) - 1))
            ligne += gscale[val]
        aaaaa.append(ligne)

    # Affichage ASCII art
    for k in range(len(aaaaa)):
        print(aaaaa[k])
    
    # enregistrement du fichier ASCII
    dl_path = os.path.join(os.path.expanduser("~"), "Downloads")
    output_file = os.path.join(dl_path, "ascii_image.txt")
    with open(output_file, "w", encoding="utf-8") as f:
        for line in aaaaa:
            f.write(line + "\n")

def img_to_ascii(image):    
    # Conversion de l'image en grayscale
    gray_scale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clarte_grille = obt_clarte(gray_scale)
    ASCII(clarte_grille)

###########################################################
import cv2
import numpy
import os

image = cv2.imread("c:/Users/Maxime/Desktop/projets/vache_2.jpg")
if image is None:
    raise ValueError("Impossible de charger l'image. Vérifie le chemin.")
else:
    img_to_ascii(image)