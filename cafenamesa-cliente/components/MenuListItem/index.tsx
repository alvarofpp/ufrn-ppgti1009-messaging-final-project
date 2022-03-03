import { View, Text, StyleSheet } from 'react-native';
import { menuListItemProps } from './types';

export default function MenuListItem(props: menuListItemProps) {
    return(
        <View style={styles.item}>
            <Text style={styles.name}>{props.name}</Text>
        </View>
    )
};

  const styles = StyleSheet.create({
      item:{
        backgroundColor: "#fff",
        padding: 15
      },
      name: {
        fontSize: 14
      },
      description: {
        fontSize: 14,
        color: "#2A2A2A"
      }
  })