import React, {useState, useEffect} from 'react'
import Table from './Table'
import Form from './Form'
import axios from 'axios'

function MyApp() {
   const [characters, setCharacters] = useState([]);

   function removeOneCharacter(index) {    
       var charDelete;
       const updated = characters.filter((character, i) => {
           if (i === index)
               charDelete = character;

           return i !== index;
       });

       makeDeleteCall(charDelete);
       setCharacters(updated);
   }

   // Called in removeOneCharacter() to send DELETE request to backend (6.4)
   async function makeDeleteCall(character) {
       try {
           const response = await axios.delete('http://localhost:5000/users', {data: {character}});
           return response;
       }
       catch (error) {
           console.log(error);
           return false;
       }
   }

   function updateList(person) {
       makePostCall(person).then(result => {
           // Frontend updating 'person' with the randomly generated id (6.3)
           person.id = result.data.user.id;

           // Response has to come with a status code of 201 for frontend state to update (6.1)
           if (result.status === 201)
              setCharacters([...characters, person]);
       });
   }

   async function fetchAll() {
       try {
           const response = await axios.get('http://localhost:5000/users');
           return response.data.users_list;
       }
       catch (error) {
           console.log(error);
           return false;
       }
   }

   async function makePostCall(person) {
       try {
           const response = await axios.post('http://localhost:5000/users', person);
           return response;
       }
       catch (error) {
           console.log(error);
           return false;
       }
   }

   useEffect( () => {
       fetchAll().then(result => {
           if (result)
              setCharacters(result);
       });
   }, [] );

   return (
       <div className="container">
           <Table characterData={characters} removeCharacter={removeOneCharacter} />
           <Form handleSubmit={updateList} />
       </div>
   )
}

export default MyApp;