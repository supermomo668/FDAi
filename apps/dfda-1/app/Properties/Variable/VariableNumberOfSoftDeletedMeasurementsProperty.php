<?php
/*
*  GNU General Public License v3.0
*  Contributors: ADD YOUR NAME HERE, Mike P. Sinn
 */

namespace App\Properties\Variable;
use App\Models\Measurement;
use App\Models\Variable;
use App\Traits\PropertyTraits\VariableProperty;
use App\Properties\Base\BaseNumberOfSoftDeletedMeasurementsProperty;
class VariableNumberOfSoftDeletedMeasurementsProperty extends BaseNumberOfSoftDeletedMeasurementsProperty
{
    use VariableProperty;
    public $table = Variable::TABLE;
    public $parentClass = Variable::class;
}
