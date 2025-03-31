<template>
  <div>
    <input
      type="text"
      v-model="query"
      @input="searchOperadoras"
      placeholder="Buscar operadoras"
    />
    <ul>
      <li v-for="operadora in operadoras" :key="operadora.id">
        {{ operadora.nome }}
      </li>
    </ul>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      query: "",
      operadoras: [],
    };
  },
  methods: {
    async searchOperadoras() {
      if (this.query.length > 0) {
        const response = await axios.get("http://localhost:5000/operadoras", {
          params: { q: this.query },
        });
        this.operadoras = response.data;
      } else {
        this.operadoras = [];
      }
    },
  },
};
</script>
