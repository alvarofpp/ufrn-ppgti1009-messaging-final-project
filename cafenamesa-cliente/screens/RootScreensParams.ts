interface ItemProps {
    id: string,
    name: string, 
    description: string,
    price: number,
  }

export type RootStackParamList = {
    Menu: undefined;
    Item: ItemProps;
    Cart: undefined;
};