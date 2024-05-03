<template>
  <!-- display publication detail -->
  <a-modal v-model:open="open"
           width="80%"
           @cancel="onClose"
           cancelText="Close"
           :ok-button-props="{style: {display: 'none'}}"
    >
    <!-- when waiting getting detail give loading animation -->
    <a-skeleton v-if="articleDetail === null" active/>
    <template #title v-if="articleDetail">
      <h1 class="heading-title" v-html="articleDetail?.title"></h1>
    </template>
    <div v-if="articleDetail" class="article-detail">
      <div class="authors">
      <div class="authors-list">
        <!-- display all author -->
        <template v-for="(author, authorIndex) in articleDetail?.author_list" :key="'author_'+authorIndex">
          <span class="authors-list-item">
            <p class="full-name">{{ author.fore_name }}&nbsp;{{ author.last_name }}</p>
          </span>
          <span class="comma" v-if="authorIndex < (articleDetail.author_list.length-1)">,&nbsp;</span>
        </template>
      </div>
    </div>
      <p>PMID: {{articleDetail.PMID}}</p>
      <!-- external link -->
      <p><a :href="'https://pubmed.ncbi.nlm.nih.gov/'+ articleDetail.PMID">https://pubmed.ncbi.nlm.nih.gov/{{articleDetail.PMID}}</a></p>
      <p><strong>Journal:</strong> {{articleDetail?.journal}}</p>
      <p><strong>Publication Year:</strong> {{articleDetail?.publication_year}}</p>
      <div class="abstract">
        <h2 class="title">Abstract</h2>
        <div class="abstract-content">
          <!-- display all abstract, some with label some not -->
          <p v-for="abstractText in abstractList" v-html="abstractText.content"></p>
        </div>
      </div>
      <p><strong>Mesh Terms: </strong> {{articleDetail?.mesh_terms.toString()}}</p>
    </div>
  </a-modal>
</template>

<script setup lang = "ts">
import { ref, computed } from 'vue'
import { IArticleDetail } from '../types'
import { getArticleDetail } from '../api'
//define variable
const open = ref<boolean>(false)
const articleDetail = ref<IArticleDetail | null>(null);
const abstractList = computed(() => {
return articleDetail.value?.abstract?.map((v)=>{
  if (![null, undefined, ''].includes(v.label)){
    v.content = `<strong class="sub-title">${v.label}:</strong>${v.content}`
  }
  return v;
}) || [];
});

//function process open event
function onOpen(id: string){
  open.value = true;
  // calling api get article information
  getArticleDetail(id).then((response) => {
    articleDetail.value = response.data.length > 0 ? response.data[0] : null;
  });
};
//function process close event
function onClose() {
  open.value = false;
  articleDetail.value = null;
};
//let parent module accessable
defineExpose({
  onOpen
});
</script>

<style lang="less" scoped>
.heading-title {
  font-size: 2.6rem;
  line-height: 1.4;
  margin: 0 0 .8rem;
  word-wrap: break-word;
}
.authors-list {
  display: inline;
  line-height: 1.5;
  margin-bottom: 1.2rem;
  .authors-list-item{
    display: inline-block;
  }
}
.abstract{
  margin:.4rem 0 0;
  word-break: break-word;
  position: relative;
  font-family: BlinkMacSystemFont, -apple-system, "Segoe UI", "Roboto", "Oxygen", "Ubuntu", "Cantarell", "Fira Sans", "Droid Sans", "Helvetica Neue", sans-serif;
  font-size: 16px;
}
strong{
  font-weight: bold;
}
p{
  margin: .6rem 0;
}
</style>