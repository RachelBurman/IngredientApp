import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Image, 
  TouchableWithoutFeedback, TouchableHighlight, 
  TouchableNativeFeedbackBase,Button, Alert} from 'react-native';
import React from 'react';
import { createStackNavigator } from '@react-navigation/stack';
import { NavigationContainer } from '@react-navigation/native';
import RecipeScreen from './RecipeScreen';
import IngredientPage from './IngredientPage';

const Stack = createStackNavigator();

function HomeScreen({ navigation }) {
  return (
    <Button
      title="Click Me"
      onPress={() =>
        Alert.alert("Would you like?", "Would you like a recipe or ingredient pairing?", [
          {text: "Recipe", onPress: () => navigation.navigate('Recipe')},
          {text: "Ingredient Pairing", onPress: () => navigation.navigate('Ingredient')}
        ])
      }
    />
  );
}

export default function App() {
  return (
    <NavigationContainer>
      <Stack.Navigator initialRouteName="Home">
        <Stack.Screen name="Home" component={HomeScreen} />
        <Stack.Screen name="Recipe" component={RecipeScreen} />
        <Stack.Screen name="Ingredient" component={IngredientPage} />
      </Stack.Navigator>
    </NavigationContainer>
  );
}
    // <View style={[styles.container, containerStyle]}>
    //   <Text>Hello React Native</Text>
    //   <Button 
    //     color="blue" 
    //     title="Click Me" 
    //     onPress={() => Alert.alert("Would you like?", "Would you like a recipe or ingredient pairing?", [
    //       {text: "Recipe", onPress: () => console.log("Recipe")},
    //       {text: "Ingredient Pairing", onPress: () => console.log("Ingredient Pairing")}
    //     ])}/>
    // </View>

const containerStyle = {backgroundColor: "orange"};
const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
