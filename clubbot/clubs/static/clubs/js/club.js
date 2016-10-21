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

Vue.component('delete-club-modal', {
    props: ['clubId'],

    methods: {
        deleteClub: function () {
            var that = this;
            this.$http.delete('/api/v1/clubs/' + that.clubId + '/')
            .then(function (response) {
                $(that.$el).modal('hide');
                if (response.ok && response.status === 204) {
                    window.location = '/account';
                }
            });
        }
    }
});

Vue.component('slug-changer', {
    props: ['club'],
    data: function () {
        return {
            errors: {
                slug: []
            }
        };
    },
    methods: {
        change: function () {
            var that = this;
            var body = {
                slug: this.club.slug
            };
            this.$http.patch('/api/v1/clubs/' + this.club.id + '/', body)
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                that.errors = [];
                that.club = data;
                window.location = '/clubs/' + data.slug;
            })
            .catch(function (error) {
                return error.json();
            }).then(function (data) {
                console.log(data);
                that.errors = data;
            });
        }
    }
});

Vue.component('club-settings', {
    props: ['clubId'],
    data: function () {
        return {
            club: null
        };
    },
    mounted: function () {
        var that = this;
        this.$http.get('/api/v1/clubs/' + this.clubId)
            .then(function (response) {
                return response.json();
            })
            .then(function (data) {
                that.club = data;
            });
    }
});

new Vue({
    el: '#club-app',
});