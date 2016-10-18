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
        fetch('/api/v1/clubs/' + this.clubId + '/cash', {
            credentials: 'same-origin'
        }).then(function (response) {
            return response.json();
        }).then(function (data) {
            that.cash = data;
        });

        fetch('/api/v1/clubs/' + this.clubId + '/cash/transactions', {
            credentials: 'same-origin'
        }).then(function (response) {
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
    el: '#club-app'
});