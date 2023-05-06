import streamlit as st

st.title('Concentration Calculator')

option = st.selectbox('Menghitung Konsentrasi',
                      ['Normalitas', 'Molaritas', 'Molalitas'])

if option == 'Normalitas':
  gram = st.number_input('Massa zat (gram):', min_value=0.0, step=0.1, value=0.1)
  liter = st.number_input('Volume (L):', min_value=0.0, step=0.1, value=0.1)
  berat_ekivalen = st.number_input('berat ekivalen (g/Grek):', min_value=0.0, step=0.1, value=0.1)        

  if st.button('Hitung'):
    normalitas = gram / (liter * berat_ekivalen)
    st.write(f'Normalitas : gram / (liter x berat ekivalen)')
    st.write(f'Normalitas : {gram} / ({liter} x {berat_ekivalen})')
    st.write(f'Normalitas: {normalitas} N (grek/L)')
    
    
elif option == 'Molaritas':

  def calculate_molarity(mass, molecular_weight, volume):
    molarity = (mass / molecular_weight) * (1000 / volume)
    return molarity

  mass = st.number_input('Massa zat (gram)', min_value=0.0, step=0.1, value=0.1)
  molecular_weight = st.number_input('Molekul relatif (g/mol)', min_value=0.0, step=0.1, value=0.1)
  volume = st.number_input('Volume larutan (mL)', min_value=0.0, step=0.1, value=0.1)

  if st.button('Hitung'):
    molarity = calculate_molarity(mass, molecular_weight, volume)
    st.write(f'Molaritas : (Massa zat / molekul relatif) x (1000 / volume)')
    st.write(f'Molaritas : ({mass} / {molecular_weight}) / ({1000} x {volume})')    
    st.write(f'Molaritas = {molarity:.2f} M (mol/L)')

else:

  def calculate_molality(mass_solvent, mol_solute, mol_weight_solute):
    molality = ((mass_solvent / mol_solute) * (1000 /mol_weight_solute))
    return molality

  mass_solvent = st.number_input('Massa zat (gram): ', min_value=0.0, step=0.1, value=0.1)
  mol_solute = st.number_input('Molekul relatif (g/Grek): ', min_value=0.0, step=0.1, value=0.1)
  mol_weight_solute = st.number_input('Massa zat pelarut (gram): ', min_value=0.0, step=0.1, value=0.1)

  if st.button("Hitung"):
    molality = calculate_molality(mass_solvent, mol_solute, mol_weight_solute)
    st.write(f'Molalitas : (Massa zat / molekul relatif) x (1000 / massa zat pelarut)')
    st.write(f'Molalitas : ({mass_solvent} / {mol_solute}) / ({1000} x {mol_weight_solute})')    
    st.write(f"The molality of the solution is {molality} m (mol/Kg)")
