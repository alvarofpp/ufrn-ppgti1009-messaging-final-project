import React from 'react';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import MenuList from './screens/Menu'; 
import { NavigationContainer } from '@react-navigation/native';
import { createNativeStackNavigator } from '@react-navigation/native-stack';
import 'react-native-gesture-handler';

import Menu from './screens/Menu';
import Item from './screens/Item';
import Cart from './screens/Cart';

import { RootStackParamList } from './screens/RootScreensParams';
import { CartProvider } from './context/CartContext';


const Stack = createNativeStackNavigator<RootStackParamList>();

export default function App() {
  return (
    <View style={{flex: 1}}>
      <CartProvider>
      <NavigationContainer >
        <Stack.Navigator >
          
            <Stack.Screen 
            name="Menu"
            component={Menu}/>
            <Stack.Screen 
            name="Item"
            component={Item}/>
            <Stack.Screen 
            name="Cart"
            component={Cart}/>
        </Stack.Navigator>
        
      </NavigationContainer>
    <StatusBar style="auto" />
    </CartProvider>
    </View> 
  )
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
    paddingTop:50
  },
});
