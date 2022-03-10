import { useNavigation, RouteProp } from '@react-navigation/native';
import { useState } from 'react';
import { View, Text, StyleSheet, Button, TouchableHighlight, Pressable } from 'react-native';
import { TouchableOpacity } from 'react-native-gesture-handler';
import { useCart } from '../../hooks/useCart';


import formatPrice from '../../utils/formatPrice';
import { menuScreenProp } from '../Menu/types';
import { RootStackParamList } from '../RootScreensParams';

interface ItemProps {
  route: ItemScreenRouteProp
}

type ItemScreenRouteProp = RouteProp<RootStackParamList, 'Item'>

export default function Item({route}: ItemProps) {
    const [amount, setAmount] = useState<number>(0);
    const cart = useCart();

    function addTotalItems(): void {
      setAmount(amount + 1);
    }

    function subTotalItems(): void{
      if(amount > 0) {
        setAmount(amount - 1);
      }
    }

    function pushToCart(id: string, amount:number, price: number): void{
      cart.addProduct({itemId: id, amount, price})
    }

    const {description, id, name, price} = route.params;
    return(
        <View style={{flex: 1, justifyContent: 'space-between'}}>
          <View>
            <Text style={styles.name}>{name}</Text>
            <Text style={styles.description}>{description}</Text>
            <Text style={styles.price}>{formatPrice(price)}</Text>

            <View style={styles.buttonGroup}>
              <Pressable style={styles.itemsNumberButton} onPress={subTotalItems}>
                <Text style={styles.itemsNumberButtonText}>-</Text>
              </Pressable>
              <Pressable style={styles.itemsNumberButton} onPress={addTotalItems}>
                <Text style={styles.itemsNumberButtonText}>+</Text>
              </Pressable>
            </View>

            <Text style={styles.resume}>Quantidade: {amount}</Text>
            <Text style={styles.resume}>Total: {formatPrice(amount * price)}</Text>
            
          </View>
            
            <Pressable style={styles.addCartButton} onPress={() => {pushToCart(id, amount, amount* price)}}>
              <Text style={styles.itemsNumberButtonText}>Adicionar ao carrinho</Text>
            </Pressable>
            
        </View>
    )
}; 

  const styles = StyleSheet.create({
      name: {
        fontSize: 18,
        fontWeight: "bold",
        color: "#000000",
        paddingLeft: 12,
        paddingTop: 10
      },
      description: {
        fontSize: 14,
        color: "#2e2e2e",
        paddingLeft: 12,
        paddingTop: 10
      },
      resume: {
        fontSize: 18,
        color: "#2e2e2e",
        paddingLeft: 12,
        paddingTop: 10
      },
      price: {
        fontSize: 18,
        color: "#02cf57",
        fontWeight: 'bold',
        marginTop:5,
        paddingLeft: 12,
      },
      buttonGroup: {
        display: 'flex',
        flexDirection: 'row',
        justifyContent: 'space-around'
      },
      addCartButton: {
        elevation: 8,
        backgroundColor: "#d32d2d",
        borderRadius: 10,
        paddingVertical: 10,
        paddingHorizontal: 12,
        marginHorizontal: 10,
        marginBottom: 10
      },
      itemsNumberButton: {
        elevation: 8,
        backgroundColor: "#bb360e",
        borderRadius: 50,
        paddingVertical: 10,
        paddingHorizontal: 12,
        marginHorizontal:10,
        marginTop: 5,
        width: 100
      },

      itemsNumberButtonText: {
        fontSize: 18,
        color: "#fff",
        fontWeight: "bold",
        alignSelf: "center",
        textTransform: "uppercase"
      }
    
  })