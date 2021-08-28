<template>
  <div>
    CompanyInfo
    <br>
    <hr>
    {{ info }}
  </div>
</template>

<script>
export default {
  props: ['info'],
  name: 'CompanyInfo'
}
</script>