<template>
    <div>
        <p class="text-gray-400">Add the name of a movie to the list, if it exists on thepiratebay, it'll be downloaded</p>
        <input v-model="textBox" class="border-solid border-2 border-gray-800 text-gray-400 rounded bg-gray-800 h-8 self-center" />
        <button v-on:click="addToList" class="px-4 hover:bg-green-800 rounded ml-2 text-gray-400 my-2 border-solid border-2 border-gray-800">Add</button>
        <br><br>
        <div>
            <div
            v-for="(movie, index) in currentList"
            :key="index"
            class="container mx-auto md:max-w-xl bg-black rounded-lg my-2 p-4"
            >
            <span class="flex justify-between">
                <p class="text-left text-2xl text-gray-400">{{movie.title}}</p>
                <button v-if="movie.status != 'downloaded'" key="remove" v-on:click="removeItem(index)" class="w-8 h-8 text-l hover:bg-red-700 mx-2 rounded self-center border-solid border-2 border-gray-400 text-gray-400">X</button>
            </span>
                <p v-if="movie.status == 'pending'" class="text-left text-orange-500">{{movie.status}}</p>
                <p v-else class="text-left text-green-500">{{movie.status}} <br> {{movie.realTitle}}</p>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    created(){
        this.getList();
    },
 
    data() {
     return{
         textBox: "",
         currentList: []
     }
 },

 methods: {

     getList: function() {
         let jsonData = require("../../../downloads.json");
         this.currentList = jsonData.movieList;
     },

     addToList: function() {
         if(this.textBox.trim().length > 0){

             let capitalizedTitle = this.textBox.charAt(0).toUpperCase() + this.textBox.slice(1);

             this.currentList.push({
                 title: capitalizedTitle,
                 status: "pending",
                 realTitle: ""
             });

             this.textBox = "";
             this.updateJSON();
         }
     },

     removeItem: function(index) {
         this.currentList.splice(index, 1);
         this.updateJSON();
     },

     updateJSON: function() {
         var JSONString = JSON.stringify(this.currentList);

         axios.post('https://0.0.0.0/updateJSON/', {
             data: JSONString,
             config: {headers: {'Content-Type': 'text/plain' }},
         }).then(function(){
             alert("JSON updated");
         }).catch(function(err){
             alert("Something went wrong: " + err);
         });

     }

 }
}

</script>