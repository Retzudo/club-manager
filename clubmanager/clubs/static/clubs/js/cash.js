Vue.http.headers.common['X-CSRFToken'] = getCookie('csrftoken');
Vue.http.options.emulateJSON = true;

Vue.component('cash-table', {
    props: ['clubId'],
    data: function () {
        return {
            cash: null,
            transactions: []
        };
    },

    mounted: function () {
        var that = this;
        this.$http.get('/api/v1/clubs/' + this.clubId + '/cash')
        .then(function (response) {
            return response.json();
        }).then(function (data) {
            that.cash = data;
        });

        this.$http.get('/api/v1/clubs/' + this.clubId + '/cash/transactions')
        .then(function (response) {
            return response.json();
        }).then(function (data) {
            that.transactions = data;
        });
    },

    methods: {
        negative: function (number) {
            return number * -1;
        },
        format: function (number) {
            return number.toFixed(2);
        },
        humanDate: function (dateString) {
            return moment.utc(dateString).fromNow();
        }
    }
});

new Vue({
    el: '#cash',
});