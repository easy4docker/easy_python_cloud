<template>
    <div class="card m-1">
        <div class="card-body alert-secondary header-bg">
            <div class="container-fluid m-0">
                <div class="row">
                    <div class="col-2 p-0 m-0 text-left">
                    </div>
                    <div class="col-8 p-2 m-0 text-center">
                        <h1 class="header-title">Python Backend Cloud Tool</h1>
                    </div>
                    <div class="col-2 p-0 m-0 text-right">
                    </div>
                </div>
            </div>
        </div> 
    </div>
</template>
 
<script>
module.exports = {
    data: function() {
        return {
            root :  this.$parent.root
        }
    },
    mounted () {
        
    },
    methods :{

    },
    components: {

    }
}
</script>
 
<style>
    .header-bg { 
    background: linear-gradient(rgba(255,255,255,0), rgba(255,255,255,0.5)),  url("/images/backend-cloud-header.png"); 
    background-repeat: no-repeat, repeat;
    background-size: cover;
    background-position: center;
    min-height: 8rem; 
    }

    .header-title {
    -webkit-text-stroke: 1px black;
    color: white;
    text-shadow:
    3px 3px 0 #000,
    -1px -1px 0 #000,  
    1px -1px 0 #000,
    -1px 1px 0 #000,
    1px 1px 0 #000;
    }
</style>
