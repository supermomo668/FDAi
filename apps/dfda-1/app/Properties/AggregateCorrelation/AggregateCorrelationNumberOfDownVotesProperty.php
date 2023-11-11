<?php
/*
*  GNU General Public License v3.0
*  Contributors: ADD YOUR NAME HERE, Mike P. Sinn
 */

namespace App\Properties\AggregateCorrelation;
use App\Models\AggregateCorrelation;
use \App\Traits\PropertyTraits\AggregateCorrelationProperty;
use App\Properties\Base\BaseNumberOfDownVotesProperty;
class AggregateCorrelationNumberOfDownVotesProperty extends BaseNumberOfDownVotesProperty
{
    use AggregateCorrelationProperty;
    public $table = AggregateCorrelation::TABLE;
    public $parentClass = AggregateCorrelation::class;
}