db.zips.aggregate([{
    $group:{
    _id:"$state",
	total_pop:{$sum:"$pop"}
	}
},
{
    $match:{
    total_pop:{$lt:1000000}}
},
{
    $out:"small_states"
}])
#to show all the collections

show collections;
