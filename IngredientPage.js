import React, {useEffect, useState} from 'react';
import { StyleSheet, Text, View, Button, Alert, Image, FlatList, TouchableOpacity, TextInput } from 'react-native';

export default function App() {
    const [ingedient, setPairings] = useState([]); 

    useEffect(() => {  
        fetch('http://10.0.2.2:5000/generate_random_pairings')
        .then(response => response.json())
        .then(data => setPairings(data));
    }, 
    
    console.log(ingedient),
    []);  // Added dependency array

    const containerStyle = {backgroundColor: "orange"};

    return (
        <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
          <Text>{ingedient}</Text>
        </View>
    );
}