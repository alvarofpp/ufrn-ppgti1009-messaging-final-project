import { View, Text, StyleSheet, Button, TouchableHighlight } from 'react-native';

import { useNavigation } from '@react-navigation/native';
import { NativeStackNavigationProp } from '@react-navigation/native-stack';
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';


import formatPrice from '../../../../utils/formatPrice';

interface CartItemProps {
    name: string;
    price: number;
    amount: number;
}


export default function CartItem( {name, price, amount } : CartItemProps) {
    return(
        <View >
            
              <View style={styles.item}>
                <Text style={styles.name}>{name}</Text>
                <Text style={styles.amount}>{amount}x</Text>
                <Text style={styles.price}>{formatPrice(price)}</Text>
              </View>
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
        fontSize: 14,
        color: "#02cf57"
      },
      amount: {
        fontSize: 12,
        color: "#2a2a2a"
      },
  })