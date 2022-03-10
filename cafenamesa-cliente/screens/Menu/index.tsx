
import { StyleSheet, Text, View, SectionList, Pressable } from 'react-native';
import MenuListItem from './components/MenuListItem';
import { itemsAPI } from '../../configs/api';
import { useCart } from '../../hooks/useCart';
import { useNavigation } from '@react-navigation/native';
import { menuScreenProp } from './types';

const DATA = itemsAPI.getAllItemsByMenu();

export default function Menu() {
  return (
    <View>
      <SectionList
        sections={DATA}
        keyExtractor={(item, index) => item.name + index}
        renderItem={({ item }) => 
          <MenuListItem 
            name={item.name} 
            price={item.price} 
            description={item.description}
            id={item.id}
            />}
        renderSectionHeader={({ section: { title } }) => (
          <Text style={styles.title}>{title}</Text>
        )}
        style={styles.list}
        />
      
          <Button></Button>
    </View>
  );
}

function Button(): JSX.Element {
  let {cart} = useCart();
  const navigation = useNavigation<menuScreenProp>();

  if(cart.length > 0){
    return (
      <Pressable style={styles.button} onPress={() => {navigation.navigate('Cart')}}>
        <Text style={styles.buttonText}>Finalizar compras</Text>
      </Pressable>
    )
  } else {
    return(
      <View></View>
    )
  }
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
    },
    button: {
      elevation: 8,
      backgroundColor: "#d32d2d",
      borderRadius: 10,
      paddingVertical: 10,
      paddingHorizontal: 12,
      marginHorizontal: 10,
      marginBottom: 10
    },
    buttonText: {
      fontSize: 18,
      color: "#fff",
      fontWeight: "bold",
      alignSelf: "center",
      textTransform: "uppercase"
    }
})