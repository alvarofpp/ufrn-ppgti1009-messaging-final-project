
import { StyleSheet, Text, View, SectionList, Pressable } from 'react-native';
import { itemsAPI } from '../../configs/api';
import { useCart } from '../../hooks/useCart';
import { FlatList } from 'react-native-gesture-handler';
import CartItem from './components/CartItem';
import { useEffect, useState } from 'react';
import formatPrice from '../../utils/formatPrice';


export default function Cart() {
    const [total, setTotal] = useState<number>(0);
    const [parsedCart, setParsedCart] = useState<any[]>([]);
    const {cart} = useCart()

    useEffect(() => {
        
        let partial = 0
        let parsedCartTemp = []
        for (let item of cart){
            const menuItem = itemsAPI.getItemById(item.id);
            parsedCartTemp.push({
                id: item.id,
                name: menuItem?.name,
                amount: item.amount,
                price: item.price
            })
            partial += item.price 
        }
    
        setTotal(partial)
        setParsedCart(parsedCartTemp)
    }, [])
    

    return (
    <View style={{flex:1, justifyContent: 'space-between'}}>
        <FlatList
        data={parsedCart}
        keyExtractor={(item, index) => item.id + index }
        renderItem={({ item }) => 
            
          <CartItem
          amount={item.amount}
          name={String(item.name)}
          price= { item.price}/>
        }
        style={styles.list}
        />
        
        <View>
            <Text style={styles.total}>Total: {formatPrice(total)}</Text>
            <Pressable style={styles.button} onPress={() => {}}>
                <Text style={styles.buttonText}>Finalizar compras</Text>
            </Pressable>
        </View>
    </View>
);
}


const styles = StyleSheet.create({
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
    },
    total: {
      borderColor: "#d32d2d",
      borderWidth: 1,
      borderRadius: 10,
      paddingVertical: 10,
      paddingHorizontal: 12,
      marginHorizontal: 10,
      marginBottom: 10,
      alignSelf: "center",
      fontSize: 18,
      color: "#2a2a2a",
      fontWeight: "bold",
      textTransform: "uppercase",
      backgroundColor: "#fff"
    }
})