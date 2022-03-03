import { StyleSheet, Text, View, SectionList } from 'react-native';
import MenuListItem from '../MenuListItem';

const DATA = [
  {
    title: "Pães",
    data: ["Pão francês", "Pão carteira", "Pão recife", "Pão australiano", "Baguete de frango", "Baguete de carne de sol"]
  },
  {
    title: "Salgados",
    data: ["Pastel de carne", "Pastel de frango", "Coxinha de carne", "Coxinha de frango"]
  },
  {
    title: "Doces",
    data: ["Torta de limão", "Bolo de chocolate", "Bolo de cenoura", "Brigadeiro"]
  },
  {
    title: "Bebidas",
    data: ["Café 100ml", "Cappucino 100ml", "Chocolate quente 100ml"]
  }

]
export default function MenuList() {
  return (
      <SectionList
        sections={DATA}
        keyExtractor={(item, index) => item + index}
        renderItem={({ item }) => <MenuListItem name={item} />}
        renderSectionHeader={({ section: { title } }) => (
          <Text style={styles.title}>{title}</Text>
        )}
        style={styles.list}
        />
  );
}

const styles = StyleSheet.create({
    title: {
        backgroundColor: 'red',
        color: 'white',
        fontSize: 18,
        padding: 5,
        borderRadius: 5,
    },
    list: {
        width: '95%'
    }
})