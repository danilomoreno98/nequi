"""
**********************************************************
2023-20-06
Prueba técnica Nequi - Data Engineer
Elaborado por: Danilo Hernando Moreno Gonzalez
Script correspondiente al EDA, Punto 1
**********************************************************
"""

# Importar librerias a utilizar durante el EDA
import pandas as pd

# Parameters Dataset
dir_file = "../data/online_retail_II.xlsx"
sheet_names = ["Year 2009-2010", "Year 2010-2011"]


"""
*************************************************
Methods
*************************************************
"""
# Step 1: Read dataset
def load_data(dir_file, *sheets_name):
    print("Leyendo Dataset...")
    dfs = []
    for sheet in sheets_name:
        df = pd.read_excel(dir_file, sheet_name=sheet)
        dfs.append(df)
    concatenated_df = pd.concat(dfs)
    print("Numero de registros del dataset: ", concatenated_df.shape[0])
    return concatenated_df


# Step 2: Variables Quantity and Type
def quantity_type_variables(df):
    column_names = df.columns.tolist()
    column_types = df.dtypes.tolist()
    print("\n***** 2. Exploración cantidad de variables y tipo *****")
    for column_name, column_type in zip(column_names, column_types):
            print(f"Columna: {column_name} -> Tipo: {column_type}")
    return column_names, column_types

# Step 3: Null rows
def null_values(df):
    print("\n***** 3. Exploración datos nulos *****\n",df.isnull().sum())
    return df.isnull().sum()

# Step 4: Unique Values "Invoices" & Customer ID "Invoice" "Customer ID"
def unique_values(df, column_name):
    return df[column_name].nunique()

# Step 5: Explore consistency in data
def consistency_numeric_data(df):
    print("\n***** 5. Exploración consistencia datos numericos *****")
    df_numeric = df.select_dtypes(include=['int64', 'float64'])
    print(df_numeric.describe().T)


# Metodo -- MAIN ---
def main():
    print("++++++++++++++++++++++ Inicia Main +++++++++++++++++++++++")
    # Step 1: Read dataset
    df_final = load_data(dir_file, *sheet_names)
    
    # Step 2: Variables Quantity and Type
    quantity_type_variables(df_final)
    
    # Step 3: Null rows
    null_values(df_final)

    # Step 4: Unique Values "Invoices" & Customer ID
    print("\n ***** 4. Exploración valores unicos, columna 'Invoice': {} *****".format(unique_values(df_final,"Invoice")))
    print("***** 4. Exploración valores unicos, columna 'Customer ID': {} *****".format(unique_values(df_final,"Customer ID")))

    # Step 5: Consistency_numeric_data
    consistency_numeric_data(df_final)


if __name__ == "__main__":
    main()  # Llamar función principal cuando se ejecute el archivo directamente