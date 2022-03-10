import { createContext, ReactNode, useContext, useState } from "react";
import { itemsAPI } from "../configs/api";

interface CartItem {
  id: string;
  amount: number;
  price: number;
}

interface CartProviderProps {
    children: ReactNode
}

interface UpdateProductAmount {
  itemId: string;
  amount: number;
}

interface AddProduct {
  itemId: string;
  amount: number;
  price: number;
}

interface CartContextData {
    cart: CartItem[];
    addProduct: (props: AddProduct) => Promise<void>;
    removeProduct: (itemId: string) => void;
    updateProductAmount: (props: UpdateProductAmount) => void;
  }
  
export const CartContext = createContext<CartContextData>({} as CartContextData);


export function CartProvider({ children }: CartProviderProps): JSX.Element {
    const [cart, setCart] = useState<any[]>(() => {
        return []
    })

    const addProduct = async ({itemId, amount, price}: AddProduct) => {
        try {
          const hasItemInCart = cart.find((item)=> item.id == itemId)

          if(hasItemInCart){
            updateProductAmount({itemId, amount})
          } else {
            const cartItem = {
              id: itemId,
              amount,
              price
            }
  
            setCart([...cart, cartItem])
          }
        } catch(e) {
          console.error(e)
        }
      };
    
      const removeProduct = (itemId: string) => {
        try {
          const newCart = cart.filter((item) => item.id != itemId)
          setCart([...newCart])
        } catch(e) {
          console.error(e)
        }
      };
    
      const updateProductAmount = async ({
        itemId,
        amount,
      }: UpdateProductAmount) => {
        try {
          const newCart = [...cart]
          const item = itemsAPI.getItemById(itemId);
          if(item){
            const cartItemIndex = newCart.findIndex(item => item.id == itemId)
            newCart[cartItemIndex].amount = amount
            newCart[cartItemIndex].price = amount * item.price

            setCart([...newCart])
          }
          
        } catch(e) {
          console.log(e)
        }
      };

    return (
        <CartContext.Provider
          value={{ cart, addProduct, removeProduct, updateProductAmount }}
        >
          {children}
        </CartContext.Provider>
      );
}

