<template>
  <div class="container">
    <h1>Publication Search</h1>
    <!-- search box, support search button and clean text -->
    <a-input-search
      v-model:value = "query"
      aria-placeholder="Insert Key Word"
      enter-button="Search"
      size = "large"
      @search="onSearch"
      style="width: 70%"
      :loading="loading"
      allowClear
    />
    <!-- Only display when getting articles list -->
    <a-card class="ls-card" v-if="articleList.length > 0">
      <a-table :columns = "columns"
               :data-source = "articleList"
               :loading = "loading"
               :pagination = "pagination"
               @change = "tableChange"
               bordered
      >
      <template #bodyCell="{ column, text, record }">
          <template v-if="column.key === 'title'">
            <!-- some title include special HTML tags, hence direct insert to let display correctly -->
            <a @click="onDetail(record)" v-html = text></a>
          </template>
        </template>
      </a-table>
      <!-- display publication detail -->
      <publication-info ref="publicationDetail"/>
    </a-card>
  </div>
</template>

<script setup lang="ts">
import PublicationInfo from './components/PublicationInfo.vue'
import { computed, ref, unref } from 'vue';
import { IArticle } from '../types'
import { searchArticles } from './api'
import { TableProps } from "ant-design-vue";
//Define values
const query = ref('');
const page = ref(1);
const total = ref(0);
const limit = ref(10);
const loading = ref(false);
const publicationDetail = ref();
const pagination = computed(()=>({
  total: total.value,
  current: page.value,
  limit: limit.value
}));
const articleList = ref<IArticle[]>([]);
  const columns = [
  {
    title: 'ID',
    dataIndex: 'PMID',
    key: 'PMID',
  },
  {
    title: 'Title',
    dataIndex: 'title',
    key: 'title',
  },
  {
    title: 'Year',
    dataIndex: 'publication_year',
    key: 'publication_year',
  },
];

// function for getting list by insert paramter
function getList(){
  //flag to tell function loading the data
  loading.value = true;
  //using api connect to the pyhton base server, deliver parameter
  searchArticles({query: query.value, page: page.value, limit:limit.value})
    .then((response) => { //wating for the response store the data
      const { data } = response;
      const { articles } = data;
      articleList.value = articles;
      total.value = data.total;
    }).finally(() => {
      loading.value = false; // flag complete loading data
    });
}

// function when user click search, set default page value as 1.
function onSearch(){
  page.value = 1;
  getList();
}
// control event when table has change( change how many element per/page, page number )
const tableChange: TableProps['onChange'] = (
  paginationInfo,
) => {
  page.value = paginationInfo.current as number;
  limit.value =paginationInfo.limit as number;
  getList();
};
// open the detail card of selecting publication
function onDetail(record:any){
  publicationDetail.value.onOpen(unref(record).PMID);
}
</script>

<style lang="less" scoped>
.container {
  width: 100%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

h1{
  color: black;
  font-size: 34px;
  text-shadow: 0 8px 10px gray;
  font-weight: bolder;
  text-align: center;
}
.ls-card{
  width: 90%;
  margin-top: 20px;
}
</style>
