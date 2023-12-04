# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import streamlit as st
import sqlite3


# Fonction pour créer la table de contacts dans la base de données
def create_table():
    conn = sqlite3.connect("contacts.db")
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS contacts
                 (name TEXT, address TEXT, phone TEXT, email TEXT, description TEXT)''')
    conn.commit()
    conn.close()


# Fonction pour ajouter un contact à la base de données
def add_contact(name, address, phone, email, description):
    conn = sqlite3.connect("contacts.db")
    c = conn.cursor()
    c.execute("INSERT INTO contacts VALUES (?, ?, ?, ?, ?)", (name, address, phone, email, description))
    conn.commit()
    conn.close()


# Fonction pour récupérer tous les contacts de la base de données
def get_contacts():
    conn = sqlite3.connect("contacts.db")
    c = conn.cursor()
    c.execute("SELECT * FROM contacts")
    contacts = c.fetchall()
    conn.close()
    return contacts


def add_contact_ui():
    name = st.text_input("Nom")
    address = st.text_input("Adresse")
    phone = st.text_input("Numéro de téléphone")
    email = st.text_input("Adresse e-mail")
    description = st.text_area("Description")

    if st.button("Ajouter"):
        add_contact(name, address, phone, email, description)
        st.success("Le contact a été ajouté avec succès")


def display_contact(contact):
    st.write(f"**Nom**: {contact[0]}")
    st.write(f"**Adresse**: {contact[1]}")
    st.write(f"**Numéro de téléphone**: {contact[2]}")
    st.write(f"**Adresse e-mail**: {contact[3]}")
    st.write(f"**Description**: {contact[4]}")


def main():
    st.title("Carnet d'adresses")
    create_table()

    contacts = get_contacts()

    st.subheader("Liste des contacts")
    for contact in contacts:
        if st.button(contact[0]):
            display_contact(contact)

    st.subheader("Ajouter un contact")
    add_contact_ui()


if __name__ == "__main__":
    main()