<?php
/*
*  GNU General Public License v3.0
*  Contributors: ADD YOUR NAME HERE, Mike P. Sinn
 */

namespace App\Properties\UserVariable;
use App\Models\UserVariable;
use App\Traits\PropertyTraits\UserVariableProperty;
use App\Properties\Base\BaseNumberOfCommonJoinedVariablesProperty;
class UserVariableNumberOfCommonJoinedVariablesProperty extends BaseNumberOfCommonJoinedVariablesProperty
{
    use UserVariableProperty;
    public $table = UserVariable::TABLE;
    public $parentClass = UserVariable::class;
}
