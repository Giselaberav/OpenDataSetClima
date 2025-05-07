import random

def limpieza (df):
    df["Precio"] = df["Precio"].apply(lambda arg_entrada: arg_entrada.replace("$", ""))
    return df

def fake_ventas (df):
    df["ventas"] = [i * random.randint(10000, 70000) for i in range(1, (df.shape[0] + 1))]
    df.to_csv("data/bookslist.csv", index=False)
    return df

#guardar el dataframe en un cvs en la carpeta data
def savefile(df):
    try:
        df.to_csv("data/datos_clima.csv", index=False)
    except Exception as e:
        print("An error occurred while saving the file: {e}")