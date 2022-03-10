import { View, Text, StyleSheet, Button, TouchableHighlight } from 'react-native';
import { menuListItemProps } from './types';
import { useNavigation } from '@react-navigation/native';
import { NativeStackNavigationProp } from '@react-navigation/native-stack';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';


import formatPrice from '../../../../utils/formatPrice';
import { menuScreenProp } from '../../types';


export default function MenuListItem({id, description, name, price, onPress}: menuListItemProps) {

  const navigation = useNavigation<menuScreenProp>()
  
    return(
        <View >
            <TouchableHighlight 
            onPress={() => {navigation.navigate('Item', {
              id,
              description,
              name,
              price
            })}}
               style={styles.item}
               underlayColor="#DDDDDD"> 
              <View>
                <Text style={styles.name}>{name}</Text>
                <Text style={styles.price}>{formatPrice(price)}</Text>
              </View>
            </TouchableHighlight>
        </View>
    )
}; 

  const styles = StyleSheet.create({
      item:{
        backgroundColor: "#fff",
        padding: 15,
        borderRadius: 5,
        borderColor: '#DDD',
        borderWidth: 1,
        margin: 5
      },
      name: {
        fontSize: 14,
        color: "#000000"
      },
      price: {
        fontSize: 10,
        color: "#02cf57"
      },
      description: {
        fontSize: 14,
        color: "#2A2A2A"
      }
  })