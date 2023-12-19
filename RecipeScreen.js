import React, {useEffect, useState} from 'react';
import { StyleSheet, Text, View, Button, Alert, Image, FlatList, TouchableOpacity, TextInput } from 'react-native';

export default function App() {
    const [recipes, setRecipes] = useState([]); 

    useEffect(() => {  
        fetch('http://10.0.2.2:5000/generate_random_recipe')
        .then(response => response.json())
        .then(data => setRecipes(data));
    }, 
    
    console.log(recipes),
    []);  // Added dependency array

    const containerStyle = {backgroundColor: "orange"};

    return (
        <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
          <Text>{recipes}</Text>
        </View>
    );
}